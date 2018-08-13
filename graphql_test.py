from graphene.test import Client

from service.graphql.graphql_schema import schema

client = Client(schema)


query = '''
query entityQuery {
  entity(id: "entity/company/netflix") {
    
    
    ... on CompanyDetails {
      companyName
      
      media  {
        
        ... on ShowMediaDetails {
          title
        }
        ... on MovieMediaDetail{
          title
        }
      }
    }
  }
}

'''

query1 = '''
query entityQuery {
  entity(id: "entity/company/warnerbro") {
    
    
    ... on CompanyDetails {
      companyName
      
      media (relationship: "produced") {
        
        ... on ShowMediaDetails {
          title
        }
        ... on MovieMediaDetail{
          title
        }
      }
    }
  }
}

'''

query2 = '''
query entityQuery {
  entity(id: "entity/company/mediarightscapital") {
    
    
    ... on CompanyDetails {
      companyName
      
      media (relationship: "produced") {
        
        ... on ShowMediaDetails {
          title
        }
        ... on MovieMediaDetail{
          title
        }
      }
    }
  }
}

'''

query3 = '''
query participantQuery {
  media(id: "media/movie/ocean11") {
    
    ... on MovieMediaDetail {
      title
      premier
      
      participant (relationship: "produced by") {
        
        ... on PersonDetails {
          name
          yearsActive
        }
        ... on CompanyDetails{
          companyName
        }
      }
    }
  }
}

'''

c = client.execute(query3)
print(c)
