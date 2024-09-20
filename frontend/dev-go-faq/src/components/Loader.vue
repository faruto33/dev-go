<template>
    <ContentLoader viewBox="0 0 250 110" >
      <rect x="0" y="10" rx="3" ry="3" width="250" height="15" />
      <rect x="0" y="30" rx="3" ry="3" width="250" height="15" />
      <rect x="0" y="50" rx="3" ry="3" width="250" height="15" />
      <rect x="0" y="70" rx="3" ry="3" width="250" height="15" />
      <rect x="0" y="90" rx="3" ry="3" width="250" height="15" />
      <rect x="0" y="110" rx="3" ry="3" width="250" height="15" />
    </ContentLoader>
</template>

<script>
import { ContentLoader } from 'vue-content-loader'

export default {
  components: {
    ContentLoader,
  },
}
</script>
