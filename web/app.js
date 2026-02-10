/**
 * app.js — lógica da calculadora web (simples e compostos)
 */
(function(){
  'use strict'

  const el = id => document.getElementById(id)
  const tipo = el('tipo')
  const capitalEl = el('capital')
  const taxaEl = el('taxa')
  const periodoEl = el('periodo')
  const btnCalcular = el('calcular')
  const btnLimpar = el('limpar')
  const resultado = el('resultado')
  const resCapital = el('resCapital')
  const resJuros = el('resJuros')
  const resMontante = el('resMontante')

  const fmt = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' })

  function parseNumber(s){
    if(!s) return NaN
    // aceita vírgula ou ponto
    return Number(String(s).trim().replace(/\./g,'').replace(',','.'))
  }

  function calcularSimples(C,i,t){
    const juros = C * i * t
    return {juros, montante: C + juros}
  }

  function calcularCompostos(C,i,t){
    const montante = C * Math.pow(1 + i, t)
    const juros = montante - C
    return {juros, montante}
  }

  function validar(C,i,t){
    const erros = []
    if(!isFinite(C) || C <= 0) erros.push('Capital deve ser um número maior que zero')
    if(!isFinite(i) || i < 0) erros.push('Taxa deve ser um número igual ou maior que zero')
    if(!isFinite(t) || t <= 0) erros.push('Período deve ser um número maior que zero')
    return erros
  }

  function mostrar(C,juros,montante){
    resCapital.textContent = `Capital inicial: ${fmt.format(C)}`
    resJuros.textContent = `Juros calculados: ${fmt.format(juros)}`
    resMontante.textContent = `Montante final:   ${fmt.format(montante)}`
    resultado.classList.remove('hidden')
  }

  btnCalcular.addEventListener('click', ()=>{
    const C = parseNumber(capitalEl.value)
    const taxaPercent = parseNumber(taxaEl.value)
    const t = parseNumber(periodoEl.value)
    const i = taxaPercent / 100

    const erros = validar(C,i,t)
    if(erros.length){
      alert(erros.join('\n'))
      return
    }

    let out
    if(tipo.value === 'simples'){
      out = calcularSimples(C,i,t)
    } else {
      out = calcularCompostos(C,i,t)
    }

    mostrar(C,out.juros,out.montante)
  })

  btnLimpar.addEventListener('click', ()=>{
    resultado.classList.add('hidden')
    resCapital.textContent = resJuros.textContent = resMontante.textContent = ''
  })

})();
