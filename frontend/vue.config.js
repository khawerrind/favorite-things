const BundleTracker = require('webpack-bundle-tracker');
const path = require('path');
// For check environment variables defined in .env of the file outside
// frontend root directory
require('dotenv').config({ path: path.join(__dirname, '/./../.env') });

module.exports = {
  productionSourceMap: false,
  publicPath: process.env.VUE_APP_PUBLIC_PATH || '',

  chainWebpack: config => {
    config.optimization.splitChunks(false);
    config
      .plugin('BundleTracker')
      .use(BundleTracker, [
        { filename: '../frontend/webpack-stats.json' }
      ]);
    config.resolve.alias.set('__STATIC__', 'static');
    config.devServer
      .public('http://localhost:8080')
      .host('localhost')
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .headers({ 'Access-Control-Allow-Origin': ['*'] });
  }
};
