# joi2008ho

## C（2019/08/04）

蟻本くじ引き相当。  
itertools で順当に 4 重ループだと間に合わ
ない。  
N = 10^3 なので、10^6 にするには 2 重ループまで。  
2 重ループ * 2 にして、bisect で時短。  
Hash（== set）を内包表記で使うと重複が自動で排除できる。
内包表記の展開時間のせいか、  
[x + y for x in X for y in Y]  
[xy for xy in XY if x + y < z]  
 より  
  [x + y for x in X for y in Y if x + y < z]   
  の方が速い。
