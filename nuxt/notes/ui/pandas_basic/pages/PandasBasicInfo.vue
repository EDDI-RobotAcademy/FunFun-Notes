<template>
    <v-container>
        <h2>Pandas Basic Info</h2>
        <v-list>
            <v-list-item
                v-for="pandasInfo in pandasInfoList"
                :key="pandasInfo.id"
            >
                <v-list-item-content>
                    
                </v-list-item-content>
            </v-list-item>
    </v-container>
</template>

<script>
import { defineComponent } from '@vue/composition-api'

export default defineComponent({
    setup() {
        
    },
})
</script>
