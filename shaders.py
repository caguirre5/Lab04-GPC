still_shader ='''
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

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);

}
'''

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
    pos = (modelMatrix * vec4(position + normals * sin(time)/10, 1.0)).xyz;

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position + normals * sin(time)/15, 1.0);

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

toon_shader ='''
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

funBluee_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    fragColor = texture(tex, UVs) * vec4(0.9,0.1,0.1,1.0);
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

colorExplotion_shader ='''
#version 450 core

uniform float time;

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform sampler2D tex;

void main()
{
    if (cos(time)>=0 && cos(time)<0.1){
        fragColor = texture(tex, UVs) * vec4(5.91,0.751,0.321,1.0);
    } else if (cos(time)>=0.1 && cos(time)<0.2) {
        fragColor = texture(tex, UVs) * vec4(0.815,0.215,0.415,1.0);
    } else if (cos(time)>=0.2 && cos(time)<0.3) {
        fragColor = texture(tex, UVs) * vec4(0.62,0.22,0.02,1.0);
    } else if (cos(time)>=0.3 && cos(time)<0.4) {
        fragColor = texture(tex, UVs) * vec4(0.525,0.525,0.525,1.0);
    }  else if (cos(time)>=0.4 && cos(time)<0.5) {
        fragColor = texture(tex, UVs) * vec4(0.23,0.63,0.73,1.0);
    }  else if (cos(time)>=0.5 && cos(time)<0.6) {
        fragColor = texture(tex, UVs) * vec4(0.635,0.835,0.335,1.0);
    } else if (cos(time)>=0.6 && cos(time)<0.7) {
        fragColor = texture(tex, UVs) * vec4(0.44,0.74,0.84,1.0);
    } else if (cos(time)>=0.7 && cos(time)<0.8) {
        fragColor = texture(tex, UVs) * vec4(0.045,0.445,0.245,1.0);
    } else if (cos(time)>=0.8 && cos(time)<0.9) {
        fragColor = texture(tex, UVs) * vec4(0.15,0.55,0.75,1.0);
    } else if (cos(time)>=0.9 && cos(time)<1) {
        fragColor = texture(tex, UVs) * vec4(0.45,0.75,0.375,1.0);
    } else if (cos(time)<0 && cos(time)>=-0.1) {
        fragColor = texture(tex, UVs) * vec4(0.815,0.215,0.415,1.0);
    } else if (cos(time)<-0.1 && cos(time)>=-0.2) {
        fragColor = texture(tex, UVs) * vec4(0.62,0.22,0.02,1.0);
    } else if (cos(time)<-0.2 && cos(time)>=-0.3) {
        fragColor = texture(tex, UVs) * vec4(0.525,0.525,0.525,1.0);
    }  else if (cos(time)<-0.3 && cos(time)>=-0.4) {
        fragColor = texture(tex, UVs) * vec4(0.23,0.63,0.73,1.0);
    }  else if (cos(time)<-0.4 && cos(time)>=-0.5) {
        fragColor = texture(tex, UVs) * vec4(0.635,0.835,0.335,1.0);
    } else if (cos(time)<-0.5 && cos(time)>=-0.6) {
        fragColor = texture(tex, UVs) * vec4(0.44,0.74,0.84,1.0);
    } else if (cos(time)<-0.6 && cos(time)>=-0.7) {
        fragColor = texture(tex, UVs) * vec4(0.045,0.445,0.245,1.0);
    } else if (cos(time)<-0.7&& cos(time)>=-0.8) {
        fragColor = texture(tex, UVs) * vec4(0.15,0.55,0.75,1.0);
    } else if (cos(time)<-0.9&& cos(time)>1) {
        fragColor = texture(tex, UVs) * vec4(0.45,0.75,0.375,1.0);
    } else {
        fragColor = texture(tex, UVs) * vec4(0.65,0.75,0.345,1.0);
    }
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

explote_shader ='''
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
    pos = (modelMatrix * vec4(position + normals * tan(time)/10, 1.5)).xyz;

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position + normals * tan(time)/10, 1.5);

}
'''
