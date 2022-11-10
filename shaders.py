vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals * sin(time * 3)/10, 1.0)).xyz;

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position + normals * sin(time * 3)/10, 1.0);

}
'''

fragment_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));

    fragColor = texture(tex, UVs) * intensity;
}
'''

toonshader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));

    if (intensity < 0.2) {
        intensity = 0.1;
    } else if (intensity < 0.5){
        intensity = 0.4;
    } else if (intensity < 0.8){
        intensity = 0.7;
    } else if (intensity <= 1) {
        intensity = 1;
    }

    fragColor = texture(tex, UVs) * intensity;

}
'''

funBlue_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    
    fragColor = texture(tex, UVs) * vec4(0,1,1,1.0);

}
'''

funPink_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    vec4 temp = 0;
    if (cos(time) < 0.5){
        temp = texture(tex, UVs) * vec4(0.5,0.3,0.8,0.5);
    } else {
        temp = texture(tex, UVs) * vec4(0.1,0.5,0.7,1.0);
    }

    fragColor = temp;
}
'''

size_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals * cos(time)/10, 1.5)).xyz;

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position + normals * cos(time)/10, 1.5);

}
'''

