import logging
from google.cloud import storage

def handle_exception(
    file_id,
    vai_gcs_bucket,
    run_folder,
    error_folder,
    error_message
):
    """
    Logs the error, appends the file_id to error tracking CSV, and triggers a notification.
    """
    try:
        error_df_path = f"{error_folder}/{run_folder}_errors.csv"

        logger.error(f"Error processing file {file_id}: {error_message}")

        gcs_client = storage.Client()
        bucket = gcs_client.bucket(vai_gcs_bucket)
        blob = bucket.blob(error_df_path)

        if blob.exists():
            error_df = pd.read_csv(f"gs://{vai_gcs_bucket}/{error_df_path}")
        else:
            error_df = pd.DataFrame(columns=["File_ID", "Error_Message"])

        error_df = pd.concat([error_df, pd.DataFrame([{"File_ID": file_id, "Error_Message": error_message}])], ignore_index=True)
        error_df.to_csv(f"gs://{vai_gcs_bucket}/{error_df_path}", index=False)
        logger.info(f"Logged error for file {file_id} in {error_df_path}")

    except Exception as e:
        logger.error(f"Failed to write to error tracking file: {e}")