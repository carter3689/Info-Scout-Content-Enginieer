# Info Scout Content Engineer Interview

The following Jupyter Notebook displays three functions used to gain insight from a provided dataset. The data has been taken from many customer transactions and aggregated to find specific insights.

The functions found in this module are as follows:
* retail_affinity: **Used to find brand affinity (given a focus brand)**
* count_hhs: **This function takes in 4 parameters -- retailer,brand,start_date,end_date. If a start/end date can not be found, the function defaults to the current date. | This function will be used to identify buying habits of customers**
* top_buying_brand: **This function will be used to find the top selling brand based on Units sold(qty) * Unit Price(amount)

# Creating Virtual Environment
create a virtual envirionment using virtualenv

* To install virtualenv use:
```shell
pip install virtualenv venv
```

* To start virtualenv:
- (Windows)
```shell
foo\bar\venv\Scripts\activate
```
-(Mac)
```shell
source venv/bin/activate
```

### Next steps:
- Navigate to working directory
- run ```pip install -r requirements.txt```
* To run the project
- run ```jupyter notebook```
* The name of the project file is: "Info Scout Content Engineer Interview.ipynb"

