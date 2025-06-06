@Suppress("DSL_SCOPE_VIOLATION")
plugins {
    id("org.jetbrains.kotlin.jvm") version "2.0.21"
    //id("com.squareup.wire") version "5.2.1"
}

group = "org.openapitools"
version = "1.0.0-SNAPSHOT"

dependencies {
    implementation("jakarta.validation:jakarta.validation-api:3.1.1")
    implementation("com.squareup.misk:misk:2025.04.27.230742-6035cb3")
    implementation("com.squareup.moshi:moshi:1.15.2")

    testImplementation("com.squareup.misk:misk-testing:2025.02.11.123913-8a41324")
    testImplementation("org.junit.jupiter:junit-jupiter:5.9.2")
}

sourceSets {
    main {
        kotlin {
            srcDirs("src/main/kotlin")
        }
        resources {
            srcDirs("src/main/resources")
        }
    }
}

/*
wire {
    sourcePath {
        srcDir("src/main/kotlin")
    }
    kotlin {
        javaInterop = true
    }
}
*/

kotlin {
    jvmToolchain(17)
}