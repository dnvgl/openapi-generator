package org.openapitools.server.api.model

import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class Tag(
    val id: kotlin.Long? = null,
    val name: kotlin.String? = null
)
