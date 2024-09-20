<template>
    <div @click="$emit('returnhome','return')" class="mayday_knowledge-breadcrumb_item bg-light">
    <div href="/" class="mayday_knowledge-breadcrumb_item_label">
      <svg fill="#000000" height="24px" width="24px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512" xml:space="preserve"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round" stroke="#CCCCCC" stroke-width="2.048"></g><g id="SVGRepo_iconCarrier"> <g> <g> <path d="M256,2.938l-256,256v48.427h62.061v201.697h155.152V384.941h77.576v124.121h155.151V307.365H512v-48.427L256,2.938z M403.394,260.82v201.697h-62.061V338.396H170.667v124.121h-62.061V260.82H63.943L256,68.762L448.057,260.82H403.394z"></path> </g> </g> </g></svg>
    </div>
  </div>
</template>

<style scoped>
.mayday_knowledge-breadcrumb_item {
  display: flex;
  align-items: center;
}
@media (min-width: 1000px) {
  .mayday_knowledge-breadcrumb_item_label {
      font-size: 16px;
      height: 48px;
      padding: 0 20px;
  }
}

.mayday_knowledge-breadcrumb_item_label {
  background: #fff;
  border: 1px solid #dbdbdb;
  border-radius: 100px;
  color: #000;
  font-size: 14px;
  height: 35px;
  max-width: calc(100vw - 30px);
  padding: 0 15px;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.mayday_knowledge-breadcrumb_item_label {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  display: flex;
  cursor: pointer;
  align-items: center;
}

</style>
