import os
import b2sdk.v2 as b2
from pathlib import Path
import tempfile
info = b2.InMemoryAccountInfo()
b2_api = b2.B2Api(info)
import pathlib

# bucket = buckets[0]
def upload_blase(file_name):
    application_key_id = "0050cb921c6832d0000000001"
    application_key = "K005iv6jd+vNqnnq+h+PZjQCU+Zg+oU"
    b2_api.authorize_account("production", application_key_id, application_key)
    bucket = b2_api.get_bucket_by_name("yetumusic")
    buckets = b2_api.list_buckets()
    print(file_name)
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file_name.read())
        temp_file_path = temp_file.name

    image = pathlib.Path(temp_file_path)
    print(buckets)

    metadata = {"key": "value"}
    uploaded_file = bucket.upload_local_file(
        local_file=image,
        file_name=file_name.name,
        file_infos=metadata,
    )
    
    return b2_api.get_download_url_for_fileid(uploaded_file.id_)


def upload_blase_music_mp3toogg(file_name):

    application_key_id = "0050cb921c6832d0000000001"
    application_key = "K005iv6jd+vNqnnq+h+PZjQCU+Zg+oU"
    b2_api.authorize_account("production", application_key_id, application_key)
    bucket = b2_api.get_bucket_by_name("yetumusic")
    buckets = b2_api.list_buckets()
    print(file_name)
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file_name.read())
        temp_file_path = temp_file.name

    image = pathlib.Path(temp_file_path)
    

    metadata = {"key": "value"}
    uploaded_file = bucket.upload_local_file(
        local_file=image,
        file_name=file_name.name,
        file_infos=metadata,
    )
    
    return b2_api.get_download_url_for_fileid(uploaded_file.id_)
