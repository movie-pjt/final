<template>
  <div>
      <review-list-form></review-list-form>
      <review-list-item
      v-for="(review, idx) in reviews"
      :key="idx"
      :review="review"
      >
      </review-list-item>

  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
import ReviewListForm from '@/components/ReviewListForm.vue'

export default {
    name: 'ReviewList',
  components: { ReviewListForm, ReviewListItem },
  props: { reviews: Array },
}
</script>

<style>

</style>