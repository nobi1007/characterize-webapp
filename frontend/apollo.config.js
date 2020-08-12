module.exports = {
    client: {
      service: {
        name: 'graphql',
        url: 'http://localhost:4000/graphql',
		// url: 'https://pilot.chainofdemand.co/graphql',
		// url: 'https://demo.chainofdemand.co/graphql',
        // optional disable SSL validation check
        skipSSLValidation: true
      }
    }
  };

// module.exports = {
//   client: {
//     service: {
//       name: 'graphql',
//       url: 'https://bluebell.chainofdemand.co:4000/',
//       // optional disable SSL validation check
//       // skipSSLValidation: true
//     }
//   }
// };