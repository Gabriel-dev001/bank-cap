import React, { useState, useCallback } from 'react';
import { 
  View, Text, TextInput, TouchableOpacity, StyleSheet 
} from 'react-native';

import { StackNavigationProp } from '@react-navigation/stack';
import { RouteProp } from '@react-navigation/native';
import { NavigationProps } from '../navigation/types';
import { ImageBackground } from 'react-native';
import { Image } from 'react-native';

// Importa os tipos da navegação para manter o código limpo
type RootStackParamList = {
  Login: undefined;
};

type LoginScreenNavigationProp = StackNavigationProp<RootStackParamList, 'Login'>;
type LoginScreenRouteProp = RouteProp<RootStackParamList, 'Login'>;

type Props = {
  navigation: LoginScreenNavigationProp;
  route: LoginScreenRouteProp;
};

const Login: React.FC<NavigationProps<'Login'>> = ({ navigation }) => {
  return (
    <ImageBackground 
        source={require('../assets/background.jpg')}
        style={styles.background}
    >
      <View style={styles.container}>
        <Text style={styles.title}>Bank Cap</Text>
        <Text style={styles.text}>Seja bem-vindo</Text>

        <TouchableOpacity style={styles.button}>
            <Image source={require('../assets/envelope.png')} style={styles.icon}/>
            <Text style={styles.text}>Continuar com Email</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.button}>
            <Image source={require('../assets/google.png')} style={styles.icon}/>
            <Text style={styles.text}>Continuar com Google</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('Register')}>
            <Image source={require('../assets/lapis.png')} style={styles.icon}/>
            <Text style={styles.text}>       Registra-se</Text>
        </TouchableOpacity>
      </View>
    </ImageBackground>
  );
};

export default Login;

const styles = StyleSheet.create({
  background: {
    flex: 1,
    width: '100%',
    height: '100%',
  },
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 40,
    fontWeight: 'bold',
    marginBottom: 5,
    color: '#FFF',
  },
  text: {
    fontSize: 15,
    color: '#FFF', 
    fontWeight: 'bold',
    textAlign: 'center',
    opacity: 0.8,
  },
  button: {
    width: '85%',
    height: 50,
    backgroundColor: 'rgb(0, 71, 187)',
    justifyContent: "flex-start",
    alignItems: 'center',
    flexDirection: 'row', // Organiza os itens lado a lado (ícone + texto)
    borderRadius: 12, // Cantos arredondados suaves
    marginTop: 10, // Espaçamento entre os elementos
    shadowColor: '#000', // Sombra para dar profundidade
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
    paddingVertical: 12, // Espaçamento interno
    paddingHorizontal: 20,
  },
  icon: {
    width: 35, // Tamanho do ícone
    height: 50,
    marginRight: 35, // Espaço entre o ícone e o texto
  },
});