<template>
  <div class="container my-5">
		<h1>Create Article</h1>
		<article-form :article="article" action="CREATE"></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'

export default {
	name: 'ArticleCreateView',
  components: { ArticleForm },
	data() {
		return {
			article: {
				pk: null,
				title: '',
				content: '',
			}
		}
	},

}
</script>

<style>

</style>