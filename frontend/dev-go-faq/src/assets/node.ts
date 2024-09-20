// User function to encode the js file containing categories from API into js tree compatible object
export function nodesEncode(categories){
  let nodes={}
  let i=0
  for(let k in categories)
  {
    i++
    let y=0
    let childrens=[]
    for(let l in categories[k])
    {
      y++
      nodes[i.toString()+'-'+y.toString()] = {'text': l,state:{ checked : true}}
      childrens[y-0]=i.toString()+'-'+y.toString()
    }
    nodes[i.toString()] = {'text': k,state:{ opened : false, disabled: false}, children: childrens}
  }
  return nodes
}

export function nodesConfig(categories)
{
  // init variables
  let roots=[]
  let config={}
  // define root elements for the tree (convert into string)
  let i=0;for(let k in categories){roots[i]=(i+1).toString();i++}

  // define the tree config
  config={
    roots: roots,
    padding: 35,
    checkboxes: false,
    dragAndDrop: true,
    editable: true,
    openedIcon: {
      type: "class",
      class: "fas fa-folder-open",
    },
    closedIcon: {
      type: "class",
      class: "fas fa-folder",
    },
    checkedClass: "fas fa-file",
  }

  return config
}
