# open
# file = open("../config/env.yaml", encoding="utf-8")
# try:
#     a = file.read()
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     file.close()

# with open
# with open("../config/env.yaml", "r",  encoding="utf-8") as file:
#     # a = file.read()
#     for i in file.readlines():
#         print("======")
#         print(i)

# PyYaml
import yaml
from common.tools import sep, get_project_path


class GetConf:
    def __init__(self):
        # 相对路径
        # with open("../config/env.yaml", "r", encoding="utf-8") as env_file:
        # 绝对路径
        with open(get_project_path() + sep(["config", "env.yaml"], add_sep_before=True), "r", encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            # print(self.env)

    def get_username_password(self, user):
        return self.env["user"][user]["username"], self.env["user"][user]["password"]

    def get_url(self):
        return self.env["url"]

    def get_mysql_config(self):
        return self.env["mysql"]

    def get_redis(self):
        return self.env["redis"]

    def get_dingding_webhook(self):
        return self.env["dingding_webhook"]

    def get_qywx_webhook(self):
        return self.env["qywx_webhook"]

    def get_jenkins(self):
        return self.env["jenkins"]


if __name__ == '__main__':
    # GetConf()
    username, password = GetConf().get_username_password()
    print(username, password)


