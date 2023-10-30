<script>
import MessageList from '../components/MessageList.vue'

export default {
    name: 'InputBlock',
    props: ['field'],
    data() { return {} },
    components: { MessageList },
}
</script>

<template>
    <div class="input-block mt-3">
        <MessageList :input_msgs="field.errors"
                     :type="'error'"
                     :time="0"></MessageList>

        <div class="one-line-field shadow-focus shadow-hover lift-hover-anim:hover mt-2">
            <label :for="field.name">{{ field.title }}</label>
            <input :type="field.type"
                   :id="field.name"
                   :name="field.name"
                   v-model="field.value"
                   :placeholder="field.placeholder"
                   @input="field.errors = null"
                   autocomplete="on">
        </div>

        <div v-if="field.hint"
             class="hint-block mt-2">
            <p v-if="field.hint.length === 1">{{ field.hint[0] }}</p>
            <li v-else
                v-for="el in field.hint">{{ el }}</li>
        </div>
    </div>
</template>

<style scoped>
.input-block {
    display: flex;
    flex-direction: column;
}

input {
    padding: 8px;

    text-indent: 12px;
    font-size: 16px;

    border-radius: 20px;
}

label {
    font-weight: 700;
}

.one-line-field {
    display: flex;
    overflow: hidden;

    border-radius: 20px;
    border-width: 2px;
    border-style: solid;
    border-color: var(--silver1-color);
    /* #2f3336; */
    background-color: var(--silver1-color);

    transition: 0.5s ease;
    transition-property: border-color, box-shadow, transform;
}

.one-line-field:hover {
    border-color: var(--hover-color);
}

.one-line-field:focus-within {
    border-color: var(--hover-color);
    box-shadow: 0px 2px 2px 1px var(--shadow-color);
    transform: translate(0, -2px);
}

.one-line-field input {
    background-color: var(--silver2-color);
    border: none;
    width: 100%;
    padding: 8px 12px;
}


.one-line-field label {
    display: inline-block;
    min-width: min-content;
    width: 20%;

    border: none;
    padding: 8px 24px;
}
</style>