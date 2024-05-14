import papermill as pm

def execute_remote_notebook(input_notebook):
    # Exécutez le notebook et enregistrez le résultat dans un nouveau notebook
    output_notebook = input_notebook + "_executed.ipynb"
    pm.execute_notebook(
        input_notebook,
        output_notebook,
        kernel_name='python3'  # Spécifiez le nom du kernel
    )
    
    return  output_notebook  # Retourne le chemin du nouveau notebook généré



