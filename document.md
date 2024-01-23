\*\*1- db yi ligfinder verileri ile ayaga kaldiralim
2- docker exec ile fastapi yapisinin temellerini atalim

docker build . -t ubuntu22-python310-base:latest : Done
docker run --name fastapi-cont -p 8083:8000 -it -e SHELL=/bin/bash -v /home/ortak/Desktop/HCU/LIG-3/lig-3-python-backend/src:/home/tosca ubuntu22-python310-base bash : Done

- kutuphane kurulumu yaptiktan sonra docker compose down yapinca kutuphane container icinden gidiyor. kutuphabne ekleyince --build ile ayaga kaldirmak gerekiyor
  3- connection pool ile db baglantilarini optimize edelim ve DB de ilk okumamizi yapalim
  4- login ve register endpointlerini yazalim
  5- login ve register endpointlerini test edelim
  6- ligfinder ednpointleri ile test yapalim
  7- geo sqlalchemy ile db deki verileri cekelim. bakalim fonskiyonlarimiz calisiyor mu?
  8- black -l . ile git e push lamadan once kodlari standarta sokkma - https://stackoverflow.com/questions/71180810/python-black-code-formatter-is-there-any-way-to-apply-automatic-black-formatti

--- pazartesi
git e push et
su docker image guncelleme isini bak- commit ile hallederbilirz. scrip yaz. guncelleme cekersen gitsin curretn container dan image olustursun
