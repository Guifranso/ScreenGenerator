param (
  [string]$pasta_rota,
  [string]$tela_nome,
  [string]$tela_numero,
  [string]$tela_funcao,
  [string]$tela_sistema,
  [string]$tela_url
)

New-Item -ItemType file -Path "$pasta_rota\Telas\$tela_nome\index.css" -Force

$jsxText = "import React from ""react"";
import ""./index.css""

const $tela_nome = () => (

  <>
    <p> $tela_nome </p>
  </>

);

export default  $tela_nome()"
New-Item -ItemType file -Path "$pasta_rota\Telas\$tela_nome\$tela_nome.jsx" -Force
Add-Content -Path $rotaTela -Value $jsxText

$menusJsText = 
"
  ${tela_numero}: Map({
  funcao: funcoes.get('${tela_funcao}'), 
  sistema: sistemas.get('${tela_sistema}'),
    url: '${tela_url}', 
    texto: '${tela_nome}', 
    component: ${tela_nome}
  }),
"

(Get-Content "$pasta_rota\Menus.js") |
Foreach-Object {
  if ($_ -match "const menus = ") {
    $_ + $menusJsText
  }
  else {
    $_
  }
} | 
Set-Content "$pasta_rota\Menus.js"