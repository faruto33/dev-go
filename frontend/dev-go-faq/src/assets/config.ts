// get the node environment variable
export const env = process.env.NODE_ENV

// define developpement API config
const development = {
  api: "https://dev-go-faq-902037774966.europe-west1.run.app",
  type: {search:'search',category:'category'},
  limit: 10,
}

 // define prod API config
const production = {
  api: "https://dev-go-faq-902037774966.europe-west1.run.app",
  type: {search:'search',category:'category'},
  limit: 10,
}

// balance API config
const configs = {
  development,
  production,
}

// export api config
export const config = configs[env]
