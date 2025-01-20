##
##              THIS SCRIPT NEEDS TO HAVE THE yt_dlp LIBRARY DOWNLOADED FOR PYTHON
##
import os
import yt_dlp               ## Libreria que permite la descarga de videos desde Youtube en Python


download_path = os.path.join(os.path.expanduser("~"), "Downloads")  ## Obtenemos el directorio de descargas

while True:
    print("Hola, ¿que desea hacer?:\n"
          + "1. Convertir de YT a MP3\n"
          + "2. Convertir de YT a MP4\n"
          + "3. Salir") 

    num = input("Escoja el numero de la opcion que desee: ")
    try:
        num = int(num)
    except ValueError:
        print("Ingrese un número válido.")
        continue

    if num == 1:
        link = input("Ponga el enlace del video que quiere descargar como MP3: ")
        try:
            ydl_opts = {                                                       # Opciones para la descarga del archivo de audio
                "format": "bestaudio",
                "outtmpl": os.path.join(download_path, "%(title)s.%(ext)s"),  # Con esto se junta el path que teniamos antes con el titulo
                "quiet" : True,
                "postprocessors":[]
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as video:
                info_dict = video.extract_info(link)                      
                video_title = info_dict['title']                            # Se saca del video el titulo para poder saber el titulo
                video_ext = info_dict.get("ext")

                video_path = os.path.join(download_path, f"{video_title}.{video_ext}")
                os.remove(video_path)                                       # Borro los archivos que puedan ser iguales

                video.download(link)                                        # Se descarga el video
                print(f"Descargado: {video_title}.webm")

        except Exception as e:
            print(f"Error al descargar: {e}")       

    elif num == 2: 
        link= input("Ponga el enlace del video que quiere descargar como MP4: ")
        
        try:
          ydl_opts = {
            "format_sort" : ["res: 1080, ext: mp4, m4a"],
            "outtmpl" : os.path.join(download_path, "%(title)s.%(ext)s"),
            "quiet" : True
          }

          with yt_dlp.YoutubeDL(ydl_opts) as video:
            info_dict = video.extract_info(link)
            video_title = info_dict ['title']
            video_ext = info_dict.get("ext")

            video_path = os.path.join(download_path, f"{video_title}.{video_ext}")
            os.remove(video_path)

            video.download(link)
            print (f"Descargado : {video_title}.mp4")

        except ValueError:
            print(f"Error: {ValueError}")




    elif num == 3:
        print("Adiós. Espero haber sido de ayuda.")
        break

    else:
        print("Opción desconocida. Inténtelo de nuevo.")
