import os
import logging

def check_image(image_name, allowed_list):
    status = False
    try:
        split_str = image_name.split("/")
        for repos in allowed_list:
            if repos in split_str[0]:
                status = True
                break

    except Exception as exp:
        logger.warning(exp)
        return False

    return status

def get_allowed_list():
    repos = open("/opt/allowed.repo_list", "r")
    repo_list = repos.read().splitlines()
    return list(repo_list)

