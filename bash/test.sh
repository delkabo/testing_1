echo "hello $1, $2!"
#for var in "$@"; do
#    echo "$var"
#done
if [ "$#" -lt 2 ];
then
    echo " Недостаточно аргументов"
    exit 1
fi
echo "hello $1, $2!"
hello
