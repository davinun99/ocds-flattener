select 
	r.ocid,
	data['compiledRelease']['id'] as "id",
	data['compiledRelease']['tender']['id'] as "tender_id",
	data['compiledRelease']['tender']['title'] as "tender.title",
	data['compiledRelease']['tender']['status'] as "tender.status",
	data['compiledRelease']['tender']['awardCriteria'] as "tender.awardCriteria",
	data['compiledRelease']['tender']['awardCriteriaDetails'] as "tender.awardCriteriaDetails",
	data['compiledRelease']['tender']['submissionMethod'] as "tender.submissionMethod",
	data['compiledRelease']['tender']['bidOpening']['date'] as "tender.bidOpening.date",
	data['compiledRelease']['tender']['bidOpening']['address']['streetAddress'] as "tender.bidOpening.address.streetAddress",
	data['compiledRelease']['tender']['submissionMethodDetails'] as "tender.submissionMethodDetails",
	data['compiledRelease']['tender']['eligibilityCriteria'] as "tender.eligibilityCriteria",
	data['compiledRelease']['tender']['statusDetails'] as "tender.statusDetails",
	data['compiledRelease']['tender']['enquiriesAddress']['streetAddress']as "tender.enquiriesAddress.streetAddress",
	data['compiledRelease']['tender']['mainProcurementCategoryDetails'] as "tender.mainProcurementCategoryDetails",
	data['compiledRelease']['tender']['hasEnquiries'] as "tender.hasEnquiries",
	data['compiledRelease']['tender']['value']['amount'] as "tender.value.amount",
	data['compiledRelease']['tender']['value']['currency'] as "tender.value.currency",
	data['compiledRelease']['tender']['datePublished'] as "tender.datePublished",
	data['compiledRelease']['tender']['tenderPeriod']['startDate'] as "tender.tenderPeriod.startDate",
	data['compiledRelease']['tender']['tenderPeriod']['endDate'] as "tender.tenderPeriod.endDate",
	data['compiledRelease']['tender']['tenderPeriod']['durationInDays'] as "tender.tenderPeriod.durationInDays",
	data['compiledRelease']['tender']['awardPeriod']['startDate'] as "tender.awardPeriod.startDate",
	data['compiledRelease']['tender']['enquiryPeriod']['endDate'] as "tender.enquiryPeriod.endDate",
	data['compiledRelease']['tender']['enquiryPeriod']['startDate'] as "tender.enquiryPeriod.startDate",
	data['compiledRelease']['tender']['enquiryPeriod']['durationInDays'] as "tender.enquiryPeriod.durationInDays",
	data['compiledRelease']['tender']['mainProcurementCategory'] as "tender.mainProcurementCategory",	
	data['compiledRelease']['tender']['procurementMethod'] as "tender.procurementMethod",
	data['compiledRelease']['tender']['procurementMethodDetails'] as "tender.procurementMethodDetails",	
	data['compiledRelease']['tender']['procuringEntity']['id'] as "tender.procuringEntity.id",
	data['compiledRelease']['tender']['procuringEntity']['name'] as "tender.procuringEntity.name",
	data['compiledRelease']['tender']['numberOfTenderers'] as "tender.numberOfTenderers",
	data['compiledRelease']['language'] as "language",	
	data['compiledRelease']['ocid'] as "ocid",
	data['compiledRelease']['date'] as "date",
	data['compiledRelease']['initiationType'] as "initiationType",
	data['compiledRelease']['buyer']['id'] as "buyer.id",
	data['compiledRelease']['buyer']['name'] as "buyer.name",
	data['compiledRelease']['planning']['identifier'] as "planning.identifier",
	data['compiledRelease']['planning']['estimatedDate'] as "planning.estimatedDate",
	data['compiledRelease']['planning']['budget']['description'] as "planning.budget.description",
	data['compiledRelease']['planning']['budget']['amount']['currency'] as "planning.budget.amount.currency",
	data['compiledRelease']['planning']['budget']['amount']['amount'] as "planning.budget.amount.amount",
	data['compiledRelease']['tag'] as "tag",
	data['compiledRelease']['tender']['coveredBy'] as "tender.coveredBy",
	data['compiledRelease']['tender']['techniques']['hasElectronicAuction'] as "tender.techniques.hasElectronicAuction",
	data['compiledRelease']['tender']['contractPeriod']['durationInDays'] as "tender.contractPeriod.durationInDays",
	data['compiledRelease']['tender']['contractPeriod']['maxExtentDate'] as "tender.contractPeriod.maxExtentDate",
	data['compiledRelease']['tender']['procurementMethodRationale'] as "tender.procurementMethodRationale",
	data['compiledRelease']['tender']['procurementIntention']['id'] as "tender.procurementIntention.id",
	data['compiledRelease']['tender']['procurementIntention']['uri'] as "tender.procurementIntention.uri",
	data['compiledRelease']['tender']['procurementIntention']['rationale'] as "tender.procurementIntention.rationale",
	data['compiledRelease']['tender']['procurementIntention']['category'] as "tender.procurementIntention.category",
	data['compiledRelease']['tender']['procurementIntention']['title'] as "tender.procurementIntention.title",
	data['compiledRelease']['tender']['procurementIntention']['description'] as "tender.procurementIntention.description",
	data['compiledRelease']['tender']['procurementIntention']['startDate'] as "tender.procurementIntention.startDate",
	data['compiledRelease']['tender']['procurementIntention']['publishedDate'] as "tender.procurementIntention.publishedDate",
	data['compiledRelease']['tender']['procurementIntention']['procuringEntity']['id'] as "tender.procurementIntention.procuringEntity.id",
	data['compiledRelease']['tender']['procurementIntention']['procuringEntity']['name'] as "tender.procurementIntention.procuringEntity.name",
	data['compiledRelease']['tender']['procurementIntention']['status'] as "tender.procurementIntention.status",
	data['compiledRelease']['tender']['procurementIntention']['statusDetails'] as "tender.procurementIntention.statusDetails",
	data['compiledRelease']['secondStage']['id'] as "secondStage.id",
	data['compiledRelease']['tender']['techniques']['hasFrameworkAgreement'] as "tender.techniques.hasFrameworkAgreement",
	data['compiledRelease']['tender']['contractPeriod']['startDate'] as "tender.contractPeriod.startDate",
	data['compiledRelease']['tender']['contractPeriod']['endDate'] as "tender.contractPeriod.endDate",
	data['compiledRelease']['planning']['budget']['budgetBreakdown'] as "planning.budget.budgetBreakdown", -- IS AN ARRAY
	data['compiledRelease']['tender']['additionalProcurementCategories'] as "tender.additionalProcurementCategories", --IS AN ARRAY
	data['compiledRelease']['tender']['lots'] as "tender.lots", --IS AN ARRAY
	data['compiledRelease']['tender']['items'] as "tender.items", --IS AN ARRAY
	data['compiledRelease']['tender']['criteria'] as "tender.criteria", --IS AN ARRAY
	data['compiledRelease']['tender']['documents'] as "tender.documents", --IS AN ARRAY FLATTENIZADO 2.1
	data['compiledRelease']['tender']['tenderers'] as "tender.tenderers", --IS AN ARRAY
	data['compiledRelease']['tender']['notifiedSuppliers'] as "tender.notifiedSuppliers", --IS AN ARRAY
	data['compiledRelease']['awards'] as "awards", --IS AN ARRAY
	data['compiledRelease']['parties'] as "parties", --IS AN ARRAY
	data['compiledRelease']['sources'] as "sources", --IS AN ARRAY
	data['compiledRelease']['contracts'] as "contracts", --IS AN ARRAY
	data['compiledRelease']['complaints'] as "complaints", --IS AN ARRAY

	-- FLATENIZACION 
		-- COMPLAINTS: 1
			CASE WHEN data['compiledRelease']['complaints'] IS NULL THEN 'No' ELSE 'Yes' END AS "has_complaints",

		-- TENDER: 2
		-- DOCUMENTS: 2.1
			data['compiledRelease']['tender']['documents']



FROM RECORD r join data d on d.id = r.data_id 
LIMIT 10