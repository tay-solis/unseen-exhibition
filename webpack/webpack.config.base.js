const path = require("path");

module.exports = {
  module: {
    rules: [
      {
        test: /\.(js)$/,
        exclude: /node_modules/,
        use: ["babel-loader"],
      },
      {
        test: /\.s[ac]ss$/i,
        use: [
          // Creates `style` nodes from JS strings
          "style-loader",
          // Translates CSS into CommonJS
          "css-loader",
          // Compiles Sass to CSS
          "sass-loader",
        ],
      },
    ],
  },
  entry: {
    gallery: "./unseen/static/js/unseen-gallery/index",
  },
  output: {
    path: path.resolve("./unseen/static/webpack_bundles"),
    filename: "[name].bundle.js",
  },
};
