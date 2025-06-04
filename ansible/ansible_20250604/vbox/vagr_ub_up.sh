#/bin/bash
folder=$PWD
RED='\033[0;31m'
bold=$(tput bold)
vagrant_all() {
	vcomm=$1
	echo -e "${bold}--------Запуск vagrant $vcomm--------"
for x in {1..3}
do
	cd $folder/vagr_ub$x
	echo -e "${RED}${bold} +++++++ vagr_ub$x"
	vagrant $vcomm
done
#	cd $folder/vagr_ub4
#	vagrant $vcomm
#	echo "vagr_ub4"
}

echo "для запуска vagrant up Введите 1"
echo "для запуска vagrant status Введите 2"
echo "для запуска vagrant halt Введите 3"

if  [ -z $1 ]; then
	echo "Переменная не передана"
else
	echo "Переменная равна $1"
fi

if [ "$1" == "1" ]; then
	vagrant_all up
elif [ "$1" == "2" ]; then
	vagrant_all status
elif [ "$1" == "3" ]; then
        vagrant_all halt
elif [ -z "$1" ]; then
	echo "Необходимо выбрать опцию"
else
	echo "Нет такой опции"
fi
