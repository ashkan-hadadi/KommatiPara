import os
from typing import Optional

import pandas
from fastapi import APIRouter, HTTPException, Request, responses

from backend.core.config import settings

router = APIRouter()


@router.get("/")
def integrate_datasets(request: Request, client_path: str, credit_path: str,
                       countries: Optional[str] = 'United Kingdom,Netherlands') -> responses.FileResponse:
    """
    API to join two datasets, filter base on countries and after storing to a file return that file.

    :param request: input request
    :param client_path: relative path to client info dataset
    :param credit_path: relative path to client's credit info dataset
    :param countries: countries to be filtered against
    :return: binary
    """

    request.state.body.update({'client_path': client_path, 'credit_path': credit_path, 'countries': countries})
    client_dataset_path = os.path.join(settings.BASE_DIR, settings.INPUT_DATASET_DIR, client_path)
    credit_dataset_path = os.path.join(settings.BASE_DIR, settings.INPUT_DATASET_DIR, credit_path)
    countries = countries.split(',')
    try:
        client_df = pandas.read_csv(client_dataset_path)
        credit_df = pandas.read_csv(credit_dataset_path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Paths not found!")

    merged_df = client_df.merge(credit_df, on='id')
    filtered_df = merged_df.query("country in @countries")
    filtered_df = filtered_df.rename(
        columns={'id': 'client_identifier', 'btc_a': 'bitcoin_address', 'cc_t': 'credit_card_type'})
    output_path = os.path.join(settings.BASE_DIR, settings.OUTPUT_DATASET_DIR, 'output.csv')
    filtered_df.to_csv(output_path,
                       columns=['client_identifier', 'bitcoin_address', 'credit_card_type', 'email'], index=False)

    return responses.FileResponse(output_path, status_code=200)
