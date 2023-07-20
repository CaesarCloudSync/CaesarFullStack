const WebTorrent = require('webtorrent')

const client = new WebTorrent()

const magnetURI = 'magnet: ...'

client.add(magnetURI, { path: '/path/to/folder' }, function (torrent) {
  torrent.on('done', function () {
    console.log('torrent download finished')
  })
})