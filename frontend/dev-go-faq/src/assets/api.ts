  //define the url to use for calling API
export default function getApi(type:string,keywords:string,category:string,config){
  let url = new URL(config.type[type], config.api)
  url.searchParams.append("keywords",keywords);
  url.searchParams.append("category", category);
  url.searchParams.append("limit", config.limit);
  return url.href
}
