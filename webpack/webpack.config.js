const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  entry: {
    app:"./src/app.js",
    out:"./src/out.js"
  },
  output: {
    filename: '[name].[contenthash].js',
    path: path.resolve(__dirname, 'dist'),
    clean:true
  },
  plugins:[
    new HtmlWebpackPlugin({title: '管理输出',}),
  ]
};