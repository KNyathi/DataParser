# Frontend
1) Create a directory called frontend and open it
```shell
mkdir Frontend
cd Frontend
```
   
2) Start the react app
```shell
npx create-react-app frontend
```

3) Install Axios for API calls
```shell
npm install axios
```

4) Setting up routing
```shell
npm install react-router-dom
```
5) Create Docker file for Frontend
```shell
touch Dockerfile.frontend
```

6) For the User Interface (UI) we are using Material-UI. Installation command is given below
   ```shell
   npm install @mui/material @emotion/react @emotion/styled
   ```
    install the MUI styles package

   ```shell
   npm install @mui/styles
   ```
# Integration tests for frontend components

a) Install testing libraries
```shell
npm install @testing-library/react @testing-library/jest-dom jest --save-dev
```
Install Babel to transform ES6 code to common JS for Jest
```shell
npm install --save-dev @babel/core @babel/preset-env @babel/preset-react babel-jest
```

![Screenshot (253)](https://github.com/KNyathi/DataParser/assets/124944851/147059eb-5582-4982-90e5-e8790e577b2c)

### test files are labelled .test.js in components, and the app.test.js is in the react root directory.


