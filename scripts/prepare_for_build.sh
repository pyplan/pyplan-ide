
echo "Copy engine code"
cp -R ../pyplan-engine/cubepy .
cp -R ../pyplan-engine/pyplan_engine .

echo "Copy ui/dist files: (builded for desktop)"
rm -rf ./pyplan/frontend
mkdir -p ./pyplan/frontend
cp -R ../../html/cubeplan-ui/dist/* ./pyplan/frontend

