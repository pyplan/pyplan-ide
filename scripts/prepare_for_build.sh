
echo "Copy engine code"
cp -R ../pyplan-engine/cubepy .
cp -R ../pyplan-engine/pyplan_engine .

echo "Copy ui/dist files: (builded for desktop)"
rm -rf ./pyplan/frontend
mkdir -p ./pyplan/frontend
# revisar paths
#cd ../../html/cubeplan-ui
#npm run build:desktop
#cd ../../python/pyplan-ide
#cp -R ../../html/cubeplan-ui/dist/* ./pyplan/frontend

