import boto3

# Initialize interfaces
s3Client = boto3.client('s3')      # Variaveis de referencia ao S3
s3Resource = boto3.resource('s3')  

# Create byte string to send to our bucket
putMessage = b'Hi! I came from Boto3!'

# put_object - Cria um objeto no s3 do zero
response = s3Client.put_object(    
    Body = putMessage,
    Bucket = 'das-demos',
    Key = 'boto3put.txt'
)

print(response)  # retorno do comando acima

# copy - configura nome do bucket e nome do arquivo
toCopy = {
    'Bucket': 'das-demos',
    'Key': 'boto3put.txt'
}

#copia um arquivo da do bucket de origem toCopy para o bucket "das-demos" com nome no destino boto3copy.txt
# meta.client é usado quando não interagimos com o arquivo, somente estamos movendo ou copiando
s3Resource.meta.client.copy(toCopy, 'das-demos', 'boto3copy.txt')

# copy_object - copia um objeto de um bucket para outro bucket no s3, muito parecido com o anterior, porem usa s3Client 
response = s3Client.copy_object(
    Bucket = 'das-demos',  #destino
    CopySource = '/das-demos/boto3put.txt',  #bucket de origem
    Key = 'boto3copyobject.txt' # nome no destino
)

print(response)

# upload_file
boto3Upload = 'boto3upload.txt'

# aqui estamos copiando um arquivo local para o s3, boto3Upload é a var que contem o nome do arquivo a ser copiado e nomeado no destino tb
# se um caminho não é informado , então ele procura no diretório de onde o script roda.
s3Resource.meta.client.upload_file(boto3Upload, 'das-demos', boto3Upload)

# upload_fileobj - mesma coisa que o anterior mas usando s3Client
with open(boto3Upload, 'rb') as fileObj:   # carrega o arquivo em memoria em modo leitura(rb) do tipo fileObj
    response = s3Client.upload_fileobj(fileObj, 'das-demos', 'boto3uploadobj.txt')  # faz o upload do fileObj no bucket das-demos com o nome boto3uploadobj.txt
    print(response)

'''
# essa parte está comentada = exemplo de como habilitar o transfer aceleration ( onde o cloud front é ativado para o bucket)
response = s3Client.put_bucket_accelerate_configuration(
    Bucket='das-demos',
    AccelerateConfiguration={
        'Status': 'Enabled'
    }
)

print(response)
'''
