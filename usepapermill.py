import papermill as pm

def execute_remote_notebook(input_notebook):
    # Exécutez le notebook et enregistrez le résultat dans un nouveau notebook
    output_notebook = input_notebook + "_executed.ipynb"
    pm.execute_notebook(
        input_notebook,
        output_notebook,
        kernel_name='python3'  # Spécifiez le nom du kernel
    )
    
    return output_notebook  # Retourne le chemin du nouveau notebook généré

def final_notebook(input_notebook):

    if __name__ == "__main__":
        notebook_to_execute = input_notebook    # Nom du notebook à exécuter
        executed_notebook = execute_remote_notebook(notebook_to_execute)
        print("Nouveau notebook généré :", executed_notebook)
