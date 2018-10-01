# s3_acl

Para não se preocupar com as permissões no s3, basta criar um lambda com o codigo xxx e com o gatilho para s3:ObjectCreated
Toda vez que um ou mais arquivos forem adicionados no bucket, as permissões serão colocadas de acordo com o código do lambda.

