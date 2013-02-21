# Consideracoes

Estou usando Tastypie para construir a API.

Criei tres modelos (Poll, Choice, Vote).

Vote foi criado para permitir `POST` em um `Vote` que pertence a um `Choice`.


Meu desejo inicial era utilizar Ember.js, e o site apenas iria consumir a API, porem nao usaria generic views
