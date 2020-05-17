from flask import *
from playground.neural_net.nn_model.model import Model
from playground.preprocessing import generic_preprocessing as gp
from playground import app
from playground.nocache import nocache

global posted
save_path = "weka/uploads/"
exts = ["csv", "json", "yaml"]
posted = 0


# @app.route("/", methods=["GET", "POST"])
# def home():

    # model = Model()
    # model.add(2, "sigmoid")
    # model.add(4, "sigmoid")
    # model.add(1, "sigmoid")
    # model.compile("Adam", 0.01)
    # model.fit([[0, 0], [0, 1], [1, 0], [1, 1]], [[0], [1], [1], [0]], 6000)
    # print(model.predict([[0, 0], [0, 1], [1, 1], [1, 0]], [[0], [1], [0], [1]]))
    # print(model.predict([[1, 0], [0, 1], [1, 1], [0, 0]], [[1], [1], [0], [0]]))

    # return render_template('home.html')

@app.route("/", methods=["GET", "POST"])
@nocache
def home():
    if request.method == "POST":
        print('here')
        if request.form["Submit"] == "Upload":
            data = request.files["data"]
            ext = data.filename.split(".")[1]
            if ext in exts:
                session["ext"] = ext
                session["fname"] = data.filename
                data.save("playground/uploads/" + data.filename)
                df = gp.read_dataset("playground/uploads/" + data.filename)
                df.to_csv("playground/clean/clean.csv", index=False)
                session["haha"] = True
                flash(f"File uploaded successfully", "success")
            else:
                flash(f"Upload Unsuccessful. Please try again", "danger")

        elif request.form["Submit"] == "Delete":
            try:
                df = gp.read_dataset("playground/clean/clean.csv")
                df = gp.delete_column(df, request.form.getlist("check_cols"))
                df.to_csv("playground/clean/clean.csv", mode="w", index=False)
                flash(f"Column(s) deleted Successfully", "success")
            except:
                flash(f"Error! Upload Dataset", "danger")

        elif request.form["Submit"] == "Clean":
            try:
                df = gp.read_dataset("playground/clean/clean.csv")
                print(request.form["how"])
                if request.form["how"] is not "any":
                    df = gp.treat_missing_numeric(
                        df, request.form.getlist("check_cols"), how=request.form["how"]
                    )
                elif request.form["howNos"] is not None:
                    df = gp.treat_missing_numeric(
                        df,
                        request.form.getlist("check_cols"),
                        how=float(request.form["howNos"]),
                    )

                df.to_csv("playground/clean/clean.csv", mode="w", index=False)
                flash(f"Column(s) cleant Successfully", "success")
            except:
                flash(f"Error! Upload Dataset", "danger")

        elif request.form["Submit"] == "Visualize":
            global posted
            df = gp.read_dataset("playground/clean/clean.csv")

            x_col = request.form["x_col"]

            if vis.hist_plot(df, x_col):
                posted = 1

        elif request.form['Submit'] == 'preprocess':
            print('True')
            return 'True'

        if session.get("haha") is not None:
            df = gp.read_dataset("playground/clean/clean.csv")
            description = gp.get_description(df)
            columns = gp.get_columns(df)
            print(columns)
            dim1, dim2 = gp.get_dim(df)
            # df.drop(['Unnamed: 0'])
            head = gp.get_head(df)

        if request.form["Submit"] == "Upload":
            return render_template(
                "home.html",
                active="preprocess",
                title="Preprocess",
                filename=session["fname"],
                posted=posted,
                no_of_rows=len(df),
                no_of_cols=len(columns),
                dim=str(dim1) + " x " + str(dim2),
                description=description.to_html(
                    classes=[
                        "table-bordered",
                        "table-striped",
                        "table-hover",
                        "thead-light",
                    ]
                ),
                columns=columns,
                head=head.to_html(
                    classes=[
                        "table",
                        "table-bordered",
                        "table-striped",
                        "table-hover",
                        "thead-light",
                    ]
                ),
            )
        elif request.form['Submit'] == 'preprocess':
            
            return render_template(
                "preprocess.html",
                active="preprocess",
                title="Preprocess",
                filename=session["fname"],
                posted=posted,
                no_of_rows=len(df),
                no_of_cols=len(columns),
                dim=str(dim1) + " x " + str(dim2),
                description=description.to_html(
                    classes=[
                        "table-bordered",
                        "table-striped",
                        "table-hover",
                        "thead-light",
                    ]
                ),
                columns=columns,
                head=head.to_html(
                    classes=[
                        "table",
                        "table-bordered",
                        "table-striped",
                        "table-hover",
                        "thead-light",
                    ]
                ),
            )

    else:
        if session.get("haha") is not None:
            df = gp.read_dataset("playground/clean/clean.csv")
            description = gp.get_description(df)
            columns = gp.get_columns(df)
            print(columns)
            dim1, dim2 = gp.get_dim(df)
            # df.drop(['Unnamed: 0'])
            head = gp.get_head(df)
            return render_template(
                "home.html",
                active="preprocess",
                title="Preprocess",
                filename=session["fname"],
                posted=posted,
                no_of_rows=len(df),
                no_of_cols=len(columns),
                dim=str(dim1) + " x " + str(dim2),
                description=description.to_html(
                    classes=[
                        "table-bordered",
                        "table-striped",
                        "table-hover",
                        "thead-light",
                    ]
                ),
                columns=columns,
                head=head.to_html(
                    classes=[
                        "table",
                        "table-bordered",
                        "table-striped",
                        "table-hover",
                        "thead-light",
                    ]
                ),
            )
        else:
            return render_template(
                "home.html", active="preprocess", title="Preprocess",
            )