import logging
from google.cloud import storage

def generate_gcs_folders(    
        pipeline_run_name,
        vai_gcs_bucket
    ):
        try:
            logging.info("Started: generating GCS pipeline folders.")
            gcs_folders = {}
            gcs_folders['gcs_staging_folder'] = f"{pipeline_run_name}/Stagging"
            gcs_folders['gcs_intra_call_dfs_folder'] = f"{pipeline_run_name}/Stagging/IntraCallDFs"
            gcs_folders['gcs_inter_call_dfs_folder'] = f"{pipeline_run_name}/Stagging/InterCallDFs"
            gcs_folders['gcs_transcripts_folder'] = f"{pipeline_run_name}/Transcripts"
            gcs_folders['gcs_errored_folder'] = f"{pipeline_run_name}/Errored"

            # Initialize GCS Client
            gcs_client = storage.Client()
            bucket = gcs_client.bucket(vai_gcs_bucket)

            # Create empty folders directly
            for folder in gcs_folders.values():
                blob = bucket.blob(f"{folder}/")
                blob.upload_from_string("", content_type="application/x-www-form-urlencoded")
                logging.info(f"Created folder: {folder}")

            logging.info("Completed: generating GCS pipeline folders.")
            return gcs_folders

        except Exception as e:
            handle_exception("N/A", vai_gcs_bucket, pipeline_run_name, gcs_folders['gcs_errored_folder'], str(e))
   