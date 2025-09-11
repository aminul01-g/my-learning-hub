from fastapi import FastAPI, Path, HTTPException, Query
import json

# create a FastAPI instance
app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data

# define a root endpoint
@app.get("/")
def hello():
    return {"message": "Hello, World!"}

# define about endpoint
@app.get("/about")
def about():
    return {"massage": "This is a simple FastAPI application."}

# define an endpoint for viewing all data
@app.get("/view")
def view():
    data = load_data()
    return data


# define an endpoint for Path parameters
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description = "Id of the patient in DB",
                                         example = "P001")):
    # load data from JSON file
    data = load_data()
    
    # find patient by id
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')


# define an endpoint for Query parameters
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description= "Sort on the basis of hight, weight or bmi"), 
                  order: str = Query('asc', description= "Sort in ascending or descending order")):
    
    vaild_fields = ['height', 'weight', 'bmi']
    if sort_by not in vaild_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort_by field. Must be one of {vaild_fields}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Must be 'asc' or 'desc'")
    
    
    data = load_data()
    
    sort_order = True if order == 'desc' else False
    
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=(order=='desc'))
    
    return sorted_data  