from django.shortcuts import render
import os
from django.http import JsonResponse
from dotenv import find_dotenv, load_dotenv
import pandas as pd
from django.conf import settings
from langchain import OpenAI
from langchain.agents import (
    load_tools,
    initialize_agent,
    create_pandas_dataframe_agent,
    Tool,
    AgentType,
)

# Create your views here.

def home_langchain(request):
    # Obtener la lista de archivos en la carpeta media/csv
    csv_folder_path = os.path.join(settings.MEDIA_ROOT, 'csv')
    archivos_csv = [archivo for archivo in os.listdir(csv_folder_path) if archivo.endswith('.csv')]

    # Agregar la lista de archivos al contexto
    context = {
        'archivos_csv': archivos_csv,
    }

    return render(request, 'agentelangchain/LLM.html', context)

def agente_langchain(request):
    if request.method == 'POST':
        # Recibir la pregunta del usuario y el nombre del archivo CSV
        question = request.POST.get('question', '')  # Asegúrate de que el nombre coincida con el formulario HTML
        archivo_csv = request.POST.get('archivo_csv', '')  # Nombre del archivo seleccionado
        
        # Configurar la clave de la API de OpenAI
        os.environ['OPENAI_API_KEY'] = "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"

        # Ruta al archivo CSV
        csv_file_path = os.path.join(settings.MEDIA_ROOT, archivo_csv)

        if not os.path.exists(csv_file_path):
            return JsonResponse({'error': 'El archivo CSV seleccionado no existe.'})

        # Leer el archivo CSV y almacenarlo en un DataFrame de Pandas
        df = pd.read_csv(csv_file_path)

        # Crear el agente de Pandas DataFrame utilizando el modelo LLM de OpenAI y el DataFrame de Pandas
        llm = OpenAI(model="text-davinci-003", temperature=0)
        agent = create_pandas_dataframe_agent(llm, df, verbose=True)

        # Obtener la respuesta del agente basada en la pregunta del usuario
        result = agent.run(question)

        # Crea una respuesta JSON con la respuesta generada.
        response = {
            'answer': result
        }

        # Devuelve la respuesta JSON.
        return JsonResponse(response)

    return JsonResponse({'error': 'Solicitud no válida'})
