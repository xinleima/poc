import json
import os

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


# 登录注册界面
# 登出
# 项目分析界面
# 分析工作台界面
# 数据库管理
# 导入数据


# 登录注册界面
@app.route('/', methods=['GET'])
@app.route('/login', methods=['GET'])
def login_page():
    return render_template("login_page.html", title="登录")


# arguments:
#   username
#   password
@app.route('/checkLogin', methods=['POST'])
def check_login():
    username = request.values.get("username")
    password = request.values.get("password")
    remember_me = request.values.get("remember-me", "")  # 选中为on
    print("check_login() username: %s, password: %s, remember_me: %s" %
          (str(username), str(password), remember_me))

    if username == "admin" and password == "admin":
        return json.dumps({"state": 0})
    return json.dumps({"state": 1})


# arguments:
#   username
#   password
@app.route('/checkRegister', methods=['POST'])
def check_register():
    username = request.values.get("username")
    password = request.values.get("password")
    print("check_register() username: %s, password: %s" % (str(username), str(password)))
    return json.dumps({"state": 0})


# 登出
@app.route('/logout', methods=['GET'])
def logout():
    print("logout")
    return redirect(url_for("login_page"))


# 项目分析界面
# template arguments:
#   project_datas
@app.route('/project', methods=['GET'])
def project_page():
    project_datas = [
        {"project_name": "项目1", "project_id": 1},
        {"project_name": "项目2", "project_id": 2},
        {"project_name": "项目3", "project_id": 3}
    ]
    return render_template("project_analysis_page.html", projects=project_datas, title="项目分析")


# arguments:
#   project_id
@app.route('/project/detail/<project_id>', methods=['GET'])
def project_detail(project_id):
    print("project_detail() project_id: %s" % project_id)
    return "project_detail() project_id: %s" % project_id


# arguments:
#   project_id
@app.route('/project/analysis/<project_id>', methods=['GET'])
def project_analysis(project_id):
    print("project_analysis() project_id: %s" % project_id)
    return "project_analysis() project_id: %s" % project_id


# arguments:
#   project_id
@app.route('/project/download/<project_id>', methods=['GET'])
def project_download(project_id):
    print("project_download() project_id: %s" % project_id)
    return "project_download() project_id: %s" % project_id


# 分析工作台界面
@app.route('/analysisWorkspace', methods=['GET'])
def analysis_workspace():
    return render_template("analysis_workspace_page.html", title="分析工作台")


# 导入数据
@app.route('/importData/direct', methods=['GET', 'POST'])
def import_data_direct():
    if request.method == 'GET':
        msg = request.values.get("msg", "")
        return render_template("import_data_direct_page.html", title="数据导入", msg=msg)
    else:
        cur_file = request.files["datafile"]
        for chunk in cur_file.readlines():
            print(chunk)
        return redirect(url_for("import_data_direct", msg="success"))


# arguments:
#   model_id
#   norm
#   tolerance
#   shell_id
#   batch_id
#   datafile
@app.route('/importData/withArgument', methods=['GET', 'POST'])
def import_data_with_argument():
    if request.method == 'GET':
        msg = request.values.get("msg", "")
        return render_template("import_data_with_argument_page.html", title="数据导入", msg=msg)
    else:
        model_id = request.values.get("model-id")
        norm = request.values.get("norm")
        tolerance = request.values.get("tolerance")
        shell_id = request.values.get("shell-id")
        batch_id = request.values.get("batch-id")
        cur_file = request.files["datafile"]

        print("型号: %s, 规格: %s, 公差: %s, 壳号: %s, 批号: %s" %
              (model_id, norm, tolerance, shell_id, batch_id))
        for chunk in cur_file.readlines():
            print(chunk)
            return redirect(url_for("import_data_with_argument", msg="success"))


# 数据库管理
# template arguments:
#   table_names
@app.route('/dbManager', methods=['GET'])
def db_manager():
    table_names = ["表1", "表2"]
    return render_template("db_manager_page.html", title="数据库管理", table_names=table_names)


# 数据库管理
# template arguments:
#   table_data
@app.route('/dbManager/detail/<table_name>', methods=['GET'])
def db_manager_detail(table_name):
    print("db_manager_detail table_id: %s" % table_name)
    test_dict = {
        "表1": {
            "fields": ["id", "file_path", "state", "result", "create_date", "update_date"],
            "datas": [
                [1, "/root/home/data", "finish", "success", "2017-04-20 12:20:20", "2017-04-20 12:20:20"],
                [2, "/root/home/data", "finish", "success", "2017-04-20 12:20:20", "2017-04-20 12:20:20"],
                [3, "/root/home/data", "finish", "success", "2017-04-20 12:20:20", "2017-04-20 12:20:20"]
            ]
        },
        "表2": {
            "fields": ["id", "file_path"],
            "datas": [
                [1, "/root/home/data"],
                [2, "/root/home/data"],
                [3, "/root/home/data"]
            ]
        }
    }
    return json.dumps(test_dict[str(table_name)])


if __name__ == '__main__':
    app.run()
