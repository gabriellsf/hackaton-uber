const url = require("url")
const urljoin = require('url-join')

function APILocation() {
  const URL = window.location.href

  if (URL.indexOf('localhost') > 0) {
    return 'http://localhost:5000'
  }

  if (URL.indexOf('192.168') >= 0) {
    return URL.replace(/:\d+.*/, ':5000')
  }

  return 'http://meu-favorito-api.herokuapp.com/?client=' + process.env.VUE_APP_UBER_USER_ID
  // const parsedURL = url.parse(URL, false, true)
  // return urljoin(parsedURL.protocol, parsedURL.host, '')
}

export default {
  API_URL: APILocation()
}