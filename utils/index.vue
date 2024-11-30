<template>
  <div>
    <MapaDirecao ref="MapaDirecaoFilho" :marcadores="marcadores" @marcadoresSelecionados="(data) => (marcadoresSelecionados = data)"
      @distancia="(data) => (distancia = data)" @duracao="(data) => duracao = data" @days="(data) => days = data"
      @hours="(data) => hours = data" @minutes="(data) => minutes = data" />

    <div class="divSide">
      <div class="DivinputPesquisa">
        <input type="text" class="inputPesquisa" v-model="pesquisa" placeholder="Pesquisar...">
        <v-btn @click="chamarOutro">chamar</v-btn>
      </div>

      <div class="detalhes mt-3" v-if="mostrarDetalhe">
        <div class="detalheimg" :style="`background-image: url(${marcadoresSelecionados.img});`">

        </div>
        <div class="legendaDetalhes">
          <h1>{{ marcadoresSelecionados.fazenda.descricao }}</h1>
          <p> {{ marcadoresSelecionados.status }}</p>

          <v-btn class="bg-green mt-2" size="small"><span class="text-white">Traçar Rota</span></v-btn>
          <div class="verRotas mt-4">
            <v-chip>
              <div class="d-flex align-center"><v-icon>distance</v-icon> <span class="ml-2">{{ distancia
              }}Km</span></div>
            </v-chip> <br>
            <v-chip class="mt-2">
              <div class="d-flex align-center"><v-icon>schedule</v-icon> <span class="ml-2">{{ duracao
              }}</span></div>
            </v-chip>
          </div>
          <div>
            <v-btn class="bg-blue-darken-3 mt-3" width="100%" v-if="marcadoresSelecionados.status === 'transporte'"><span
                class="text-white">Solicitar
                Transporte</span></v-btn>
            <v-btn class="bg-blue-darken-3 mt-3" width="100%" v-if="marcadoresSelecionados.status === 'empresa'"><span
                class="text-white">Vender
                Produtos</span></v-btn>
            <v-btn class="bg-blue-darken-3 mt-3" width="100%" v-if="marcadoresSelecionados.status === 'insumo'"><span
                class="text-white">Ver
                Produtos</span></v-btn>
            <v-btn class="bg-blue-darken-3 mt-3" width="100%" v-if="marcadoresSelecionados.status === 'fazenda'"><span
                class="text-white">Ver
                Fazenda</span></v-btn>
          </div>
        </div>
      </div>
      <div class="divResultados" v-if="mostrarPesquisa">
        <div>
          <div class="paiResultado">
            <div class="filhoResultado" v-for="marcador, index in marcadoresFiltrados" :key="index">
              <div class="dentroFilhoResultado" @click="verMarcador(marcador)">
                <div class="legResultado">
                  <h3>{{ marcador.fazenda.descricao }}</h3>
                  <p>{{ marcador.status }}</p>
                  <v-chip size="small">{{ marcador.distancia }}km ~ {{ marcador.tempo }}
                  </v-chip>
                </div>
                <div class="DivimgResultado">
                  <div class="imgResultado" :style="`background-image: url(${marcador.img});`">

                  </div>
                </div>
              </div>
              <div class="HrFihoResultado my-3"></div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import axios from 'axios'
import { LocalizaoFazendas } from '~~/services/fazenda';
import { PontosFazenda } from '~~/services/localizacao';
const marcadoresSelecionados = ref('')
const distancia = ref(0)
const duracao = ref(0)
const days = ref(0)
const hours = ref(0)
const minutes = ref(0)
const pesquisa = ref('')
const mostrarDetalhe = ref(false)
const mostrarPesquisa = ref(false)
const MapaDirecaoFilho = ref(null)

const token = "pk.eyJ1IjoidGVjbm9iYXNlIiwiYSI6ImNsZW56eWJueTE5dXQzd29kdjZueno0cHMifQ.NHJAgCxnQ8Jtcw16ooYtjw"
const marcadores = ref([
  {
      descricao: "Fazenda Mumba",
      img: "/img/fazendas/fazenda.jpeg",
      longitude: 15.0667,
      latitude: -14.6833,
      status: "fazenda",
  },
  {
      descricao: "Grupo Carrinho",
      img: "/img/empresas/carrinho.jpeg",
      longitude: 13.4055,
      latitude: -12.5763,
      status: "empresa"
  },

  {
      descricao: "FertiAngola",
      img: "/img/empresas/fetiAngola.png",
      longitude: 15.7392,
      latitude: -12.7761,
      status: "insumo"
  },
  {
      descricao: "Fuso",
      img: "/img/carros/fuso.jpg",
      longitude: 13.2500,
      latitude: -8.8498,
      status: "transporte"
  }
])

const chamarOutro = () => {
  MapaDirecaoFilho.value.fazerTeste()
}

const verPontos = async () => {
  await PontosFazenda().then((response) => {
    console.log(response)
    marcadores.value = response
    // MapaDirecaoFilho.value.verMapa()
    
    if (navigator.geolocation) {
      // Primeiro, pegue a localização do usuário uma vez
      navigator.geolocation.getCurrentPosition(async (position) => {
        const userPosition = [position.coords.longitude, position.coords.latitude];

        // Agora, loop através dos marcadores
        for (let index = 0; index < marcadores.value.length; index++) {
          const element = marcadores.value[index];
          // console.log(element)
          // alert('ola como vai')

          await verRota(index, [element.longitude, element.latitude], userPosition);
        }
      });
    }
  })
}


//  distancia

onMounted(() => {
  verPontos()
  // if (navigator.geolocation) {
  //   // Primeiro, pegue a localização do usuário uma vez
  //   navigator.geolocation.getCurrentPosition(async (position) => {
  //     const userPosition = [position.coords.longitude, position.coords.latitude];

  //     // Agora, loop através dos marcadores
  //     for (let index = 0; index < marcadores.value.length; index++) {
  //       const element = marcadores.value[index];
  //       // console.log(element)
  //       await verRota(index, [element.longitude, element.latitude], userPosition);
  //     }
  //   });
  // }
});

const oraganizar = ref([])

onMounted(async () => {
  if (navigator.geolocation) {
    // Pegue a localização do usuário uma vez
    navigator.geolocation.getCurrentPosition(async (position) => {
      const userPosition = [position.coords.longitude, position.coords.latitude];

      // Use Promise.all para lidar com chamadas de forma concorrente
      const promises = marcadores.value.map((element, index) => {
        return verRota(index, [element.longitude, element.latitude], userPosition);
      });


      await Promise.all(promises);
    });
  }
});

watch(pesquisa, () => {
  marcadoresSelecionados.value = ''
  if (pesquisa.value.length >= 1) {
    mostrarPesquisa.value = true
    mostrarDetalhe.value = false
  } else {
    mostrarPesquisa.value = false
  }

  pesquisarMarcador(pesquisa.value)
})

watch(marcadoresSelecionados, () => {
  pesquisa.value = ''
  if (marcadoresSelecionados !== '') {
    mostrarDetalhe.value = true
    mostrarPesquisa.value = false
  } else {
    mostrarDetalhe.value = false
  }
})

const marcadoresFiltrados = ref(marcadores.value)
const pesquisarMarcador = (palavra) => {
  // console.log(palavra)
  marcadoresFiltrados.value = marcadores.value.filter(item => item.fazenda.descricao.toLowerCase().includes(palavra.toLowerCase()));
}

const verMarcador = (mark) => {
  mostrarDetalhe.value = true
  marcadoresSelecionados.value = mark
}

const verRota = async (i, fim, inicio) => {
  const rotaURL = `https://api.mapbox.com/directions/v5/mapbox/driving/${inicio[0]},${inicio[1]};${fim[0]},${fim[1]}?geometries=geojson&access_token=${token}`;

  try {
    const { data } = await axios.get(rotaURL);
    if (data && data.routes && data.routes[0]) {
      const coordenadas = data.routes[0].geometry.coordinates;
      const route = data.routes[0].geometry;
      const distancia = (data.routes[0].distance / 1000) // convertendo de metros para kilometros
      const duracao = data.routes[0].duration // convertendo de segundos para minutos

      const durationInSeconds = duracao;
      const days = Math.floor(durationInSeconds / 86400);
      const hours = Math.floor((durationInSeconds % 86400) / 3600);
      const minutes = Math.round((durationInSeconds % 3600) / 60);

      let formattedDuration = '';
      if (days > 0) formattedDuration += `${days}d `;
      if (hours > 0) formattedDuration += `${hours}h e `;
      formattedDuration += `${minutes}min`;

      // rota.value = { distancia, duracao }
      // console.log(formattedDuration)

      marcadores.value[i].tempo = formattedDuration
      marcadores.value[i].distancia = (distancia).toFixed(2)
      marcadores.value.sort((a, b) => Number(a.distancia) - Number(b.distancia))
    }
    else {
      console.warn("Unexpected API response:", data);
    }
  } catch (error) {
    console.error("Erro ao buscar os dados", error);
  }
}
const verRotas = async (i, fim) => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(async (position) => {
      const userPosition = [position.coords.longitude, position.coords.latitude];
      const primeiro = [userPosition[0], userPosition[1]]
      const rotaURL = `https://api.mapbox.com/directions/v5/mapbox/driving/${primeiro[0]},${primeiro[1]};${fim[0]},${fim[1]}?geometries=geojson&access_token=${token}`;

      try {
        const { data } = await axios.get(rotaURL)
        if (data && data.routes && data.routes[0]) {
          const coordenadas = data.routes[0].geometry.coordinates;
          const route = data.routes[0].geometry;
          const distancia = (data.routes[0].distance / 1000).toFixed(2) // convertendo de metros para kilometros
          const duracao = data.routes[0].duration // convertendo de segundos para minutos

          const durationInSeconds = duracao;
          const days = Math.floor(durationInSeconds / 86400);
          const hours = Math.floor((durationInSeconds % 86400) / 3600);
          const minutes = Math.round((durationInSeconds % 3600) / 60);

          let formattedDuration = '';
          if (days > 0) formattedDuration += `${days}d `;
          if (hours > 0) formattedDuration += `${hours}h e `;
          formattedDuration += `${minutes}min`;

          // rota.value = { distancia, duracao }
          // console.log(formattedDuration)

          marcadores.value[i].tempo = formattedDuration

          // return formattedDuration

          // Verifica e remove layers e sources antigos antes de adicionar novos
          // if (map.value.getLayer('route')) {
          //     map.value.removeLayer('route');
          // }

          // if (map.value.getSource('route')) {
          //     map.value.removeSource('route');
          // }

          // map.value.addLayer({
          //     id: 'route',
          //     type: 'line',
          //     source: {
          //         type: 'geojson',
          //         data: {
          //             type: 'Feature',
          //             properties: {},
          //             geometry: route
          //         }
          //     },
          //     layout: {
          //         'line-join': 'round',
          //         'line-cap': 'round'
          //     },
          //     paint: {
          //         'line-color': '#1db7dd',
          //         'line-width': 3
          //     }
          // });
        }
        else {
          console.warn("Unexpected API response:", data);
        }

      } catch (error) {
        console.log("erro ao buscar os dados", error)
      }
    }
    )

  }


}

</script>

<style lang="scss" scoped>
.divSide {
  position: absolute;
  width: 300px;
  top: 30px;
  right: 40px;

  .DivinputPesquisa {
    background-color: #fff;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.492);
    border-radius: 15px;

    input {
      width: 100%;
      padding: 10px;
      outline: none;
    }
  }

  .detalhes {

    background-color: #fff;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.492);
    border-radius: 15px;



    .detalheimg {
      width: 100%;
      height: 200px;
      background-color: #333;
      border-radius: 5px;
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
      border-radius: 15px 15px 0 0;
    }

    .legendaDetalhes {
      padding: 10px 20px;

      h1 {
        font-size: 20px;
        text-transform: capitalize;
      }

      p {
        font-size: 17px;
        text-transform: capitalize;
      }
    }
  }

  .divResultados {
    background-color: #fff;
    width: 100%;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.492);
    border-radius: 15px;
    margin-top: 10px;
    height: 500px;

    .filhoResultado {
      cursor: pointer;
      padding: 10px;

      &:hover {
        background-color: #f7f7f7;
      }

      .dentroFilhoResultado {
        display: flex;
        justify-content: space-between;

        .legResultado {
          h3 {
            font-size: 15px;
            font-weight: 600;
          }
        }

        .DivimgResultado {
          display: flex;
          justify-content: center;
          align-items: center;
          padding: 5px;



          .imgResultado {
            width: 100px;
            height: 75px;
            background-color: #333;
            border-radius: 15px;
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
          }
        }

      }
    }

    .HrFihoResultado {
      width: 100%;
      height: 2px;
      background-image: linear-gradient(to left, transparent, #ccc, transparent);
    }

  }
}
</style>