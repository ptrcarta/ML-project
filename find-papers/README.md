# FIND PAPERS

## Download papers in JSON format

This folder contains the code to download and parse all papers submited to the ICLR challenge at [openreview.net](https://openreview.net/group?id=ICLR.cc/2019/Conference).

### How to

- Step 1: run `./download_projects_json.sh` to download all papers in a `json` format. The data will be saved in a `list.json` document. Dependency: `jq`and `curl`
- Step 2: run `python json_explorer.py N` to display the first N papers ordered by number of replies.
