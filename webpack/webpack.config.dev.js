const path = require("path");
var MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  mode: 'development',
  plugins: [
    new MiniCssExtractPlugin({
      filename: "css/[name].css"
    }),
  ],
  module: {
    rules: [
      {
        test: /\.(js)$/,
        exclude: /node_modules/,
        use: ["babel-loader"],
      },
      // fonts
      {
        test: /\.(woff|woff2|eot|ttf|svg)$/,
        use: [
          {
            loader: "file-loader",
            options: {
              outputPath: "fonts/",
              publicPath: "../../webpack_bundles/fonts/"
            }
          }
        ]
      },
      // sass
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          "sass-loader",
        ]
      },
      // css
      {
        test: /\.css$/,
        use: [
          "style-loader",
          {
            loader: "css-loader",
            options: {
              modules: true,
              importLoaders: 1
            }
          }
        ]
      }
    ],
  },
  entry: {
    gallery: "./unseen/static/js/unseen-gallery/index",
    styles: ["./unseen/static/sass"]
  },
  output: {
    path: path.resolve("./unseen/static/webpack_bundles"),
    filename: "[name].bundle.js",
  },
};
