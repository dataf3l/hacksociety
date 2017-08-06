create table person2 as (select 
	fecha_dato            ,    
	ncodpers              ,   
	ind_empleado          ,  
	pais_residencia       , 
	sexo                  ,
	age                   ,
	fecha_alta            ,
	ind_nuevo              as es_nuevo_cliente,
	antiguedad            ,
	indrel                ,
	ult_fec_cli_1t        ,
	indrel_1mes           ,
	tiprel_1mes           ,
	indresi               ,
	indext                ,
	conyuemp              ,
	canal_entrada         ,
	indfall               ,
	tipodom               ,
	cod_prov              ,
	nomprov               ,
	ind_actividad_cliente ,
	renta                 ,
	segmento              ,
	(case when sexo = 'H' then 1 else 0 end) as es_hombre,
	(case when tiprel_1mes = 'A' then 1 else 0 end) as es_cliente_activo,
	(case when indext = 'S' then 1 else 0 end) as es_cliente_extranjero,
	(case when canal_entrada = 'KHE' then 1 else 0 end) as canal_KHE,
	(case when canal_entrada = 'KFC' then 1 else 0 end) as canal_KFC,
	(case when canal_entrada = 'KHD' then 1 else 0 end) as canal_KHD,
	(case when canal_entrada = 'KAT' then 1 else 0 end) as canal_KAT,
	(case when canal_entrada = 'KFA' then 1 else 0 end) as canal_KFA,
	(case when canal_entrada = 'KAZ' then 1 else 0 end) as canal_KAZ,
	(case when canal_entrada = 'KHC' then 1 else 0 end) as canal_KHC,
	(case when canal_entrada = 'KHK' then 1 else 0 end) as canal_KHK,
	(case when canal_entrada = 'RED' then 1 else 0 end) as canal_RED,
	(case when nomprov = 'MADRID' then 1 else 0 end) as provincia_MADRID,
	(case when nomprov = 'BARCELONA' then 1 else 0 end) as provincia_BARCELONA,
	(case when nomprov = 'PONTEVEDRA' then 1 else 0 end) as provincia_PONTEVEDRA,
	(case when nomprov = 'SEVILLA' then 1 else 0 end) as provincia_SEVILLA,
	(case when nomprov = 'VALENCIA' then 1 else 0 end) as provincia_VALENCIA,
	(case when nomprov = 'MALAGA' then 1 else 0 end) as provincia_MALAGA,
	(case when nomprov = 'MURCIA' then 1 else 0 end) as provincia_MURCIA,
	(case when nomprov = 'ZARAGOZA' then 1 else 0 end) as provincia_ZARAGOZA,
	(case when nomprov = 'CADIZ' then 1 else 0 end) as provincia_CADIZ,
	(case when nomprov = 'BADAJOZ' then 1 else 0 end) as provincia_BADAJOZ,
	(case when nomprov = 'ALICANTE' then 1 else 0 end) as provincia_ALICANTE,
	(case when nomprov = 'CASTELLON' then 1 else 0 end) as provincia_CASTELLON,
	(case when nomprov = 'HUELVA' then 1 else 0 end) as provincia_HUELVA,
	(case when nomprov = 'SALAMANCA' then 1 else 0 end) as provincia_SALAMANCA,
	(case when nomprov = 'CORDOBA' then 1 else 0 end) as provincia_CORDOBA,
	(case when nomprov = 'TOLEDO' then 1 else 0 end) as provincia_TOLEDO,
	(case when nomprov = 'CACERES' then 1 else 0 end) as provincia_CACERES,
	(case when nomprov = 'VALLADOLID' then 1 else 0 end) as provincia_VALLADOLID,
	(case when nomprov = 'LERIDA' then 1 else 0 end) as provincia_LERIDA,
	(case when nomprov = 'CANTABRIA' then 1 else 0 end) as provincia_CANTABRIA,
	(case when nomprov = 'OURENSE' then 1 else 0 end) as provincia_OURENSE,
	(case when nomprov = 'LUGO' then 1 else 0 end) as provincia_LUGO,
	(case when nomprov = 'GIRONA' then 1 else 0 end) as provincia_GIRONA,
	(case when nomprov = 'ALBACETE' then 1 else 0 end) as provincia_ALBACETE,
	(case when nomprov = 'CIUDAD REAL' then 1 else 0 end) as provincia_CIUDAD_REAL,
	(case when nomprov = 'ASTURIAS' then 1 else 0 end) as provincia_ASTURIAS,
	(case when nomprov = 'BURGOS' then 1 else 0 end) as provincia_BURGOS,
	(case when nomprov = 'GRANADA' then 1 else 0 end) as provincia_GRANADA,
	(case when nomprov = 'TARRAGONA' then 1 else 0 end) as provincia_TARRAGONA,
	(case when nomprov = 'CUENCA' then 1 else 0 end) as provincia_CUENCA,
	(case when nomprov = 'ZAMORA' then 1 else 0 end) as provincia_ZAMORA,
	(case when nomprov = 'NAVARRA' then 1 else 0 end) as provincia_NAVARRA,
	(case when nomprov = 'LEON' then 1 else 0 end) as provincia_LEON,
	(case when nomprov = 'HUESCA' then 1 else 0 end) as provincia_HUESCA,
	(case when nomprov = 'BIZKAIA' then 1 else 0 end) as provincia_BIZKAIA,
	(case when nomprov = 'PALENCIA' then 1 else 0 end) as provincia_PALENCIA,
	(case when nomprov = 'JAEN' then 1 else 0 end) as provincia_JAEN,
	(case when nomprov = 'AVILA' then 1 else 0 end) as provincia_AVILA,
	(case when nomprov = 'SEGOVIA' then 1 else 0 end) as provincia_SEGOVIA,
	(case when nomprov = 'ALMERIA' then 1 else 0 end) as provincia_ALMERIA,
	(case when nomprov = 'SANTA CRUZ DE TENERIFE' then 1 else 0 end) as provincia_SANTA_CRUZ_DE_TENERIFE,
	(case when nomprov = 'GUADALAJARA' then 1 else 0 end) as provincia_GUADALAJARA,
	(case when nomprov = 'TERUEL' then 1 else 0 end) as provincia_TERUEL,
	(case when nomprov = 'GIPUZKOA' then 1 else 0 end) as provincia_GIPUZKOA,
	(case when nomprov = 'SORIA' then 1 else 0 end) as provincia_SORIA,
	(case when nomprov = 'ALAVA' then 1 else 0 end) as provincia_ALAVA,
	(case when nomprov = 'MELILLA' then 1 else 0 end) as provincia_MELILLA,
	(case when nomprov = 'CEUTA' then 1 else 0 end) as provincia_CEUTA,
	(case when segmento = '03 - UNIVERSITARIO' then 1 else 0 end) as es_universitario,
	(case when segmento = '02 - PARTICULARES' then 1 else 0 end) as es_particular,
	(case when segmento = '01 - TOP' then 1 else 0 end) as es_top,
	trim(ind_ahor_fin_ult1) as ind_ahor_fin_ult1,
	trim(ind_aval_fin_ult1) as ind_aval_fin_ult1,
	trim(ind_cco_fin_ult1) as ind_cco_fin_ult1,
	trim(ind_cder_fin_ult1) as ind_cder_fin_ult1,
	trim(ind_cno_fin_ult1) as ind_cno_fin_ult1,
	trim(ind_ctju_fin_ult1) as ind_ctju_fin_ult1,
	trim(ind_ctma_fin_ult1) as ind_ctma_fin_ult1,
	trim(ind_ctop_fin_ult1) as ind_ctop_fin_ult1,
	trim(ind_ctpp_fin_ult1) as ind_ctpp_fin_ult1,
	trim(ind_deco_fin_ult1) as ind_deco_fin_ult1,
	trim(ind_deme_fin_ult1) as ind_deme_fin_ult1,
	trim(ind_dela_fin_ult1) as ind_dela_fin_ult1,
	trim(ind_ecue_fin_ult1) as ind_ecue_fin_ult1,
	trim(ind_fond_fin_ult1) as ind_fond_fin_ult1,
	trim(ind_hip_fin_ult1) as  ind_hip_fin_ult1,
	trim(ind_plan_fin_ult1) as ind_plan_fin_ult1,
	trim(ind_pres_fin_ult1) as ind_pres_fin_ult1,
	trim(ind_reca_fin_ult1) as ind_reca_fin_ult1,
	trim(ind_tjcr_fin_ult1) as ind_tjcr_fin_ult1,
	trim(ind_valo_fin_ult1) as ind_valo_fin_ult1,
	trim(ind_viv_fin_ult1) as  ind_viv_fin_ult1,
	trim(ind_nomina_ult1) as   ind_nomina_ult1,
	trim(ind_nom_pens_ult1) as ind_nom_pens_ult1,
	trim(ind_recibo_ult1) as   ind_recibo_ult1
	

FROM 
	person
where 
	ind_empleado = 'N')



