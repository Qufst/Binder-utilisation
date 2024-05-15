import papermill as pm

def execute_remote_notebook(input_notebook):
    # Exécutez le notebook et enregistrez le résultat dans un nouveau notebook
    output_notebook = input_notebook + "_executed.ipynb"
    binder_link = "https://notebooks.gesis.org/binder/jupyter/user/qufst-projet-personnel-m-t-o-7ioms0h0/lab/tree/Untitled.ipynb"
    pm.execute_notebook(
        input_notebook,
        output_notebook,
        parameters={"binder_link": binder_link},
        kernel_name='python3'  # Spécifiez le nom du kernel
    )
    
    return  output_notebook  # Retourne le chemin du nouveau notebook généré



